const express = require('express')
const cheerio = require('cheerio')
const request = require('request')

const matchBikeRe = /bike|bicycle/i
const matchIdRe = /\(\#(\d)+\)/
const matchTitleRe = /\).*?See details/

const SCRAPING_INTERVAL = 60 * 1000 // 1 minute.

const groups = [
  "BarkingandDagenham", "BarnetUK", "BexleyUK", "BrentUK", "BromleyUK", "HampsteadUK", "KentishtownUK", "CamdenSouthUK", "CityOfLondon",
  "CroydonUK", "EalingUK", "EnfieldUK", "Feltham-Bedfont-HanworthUK", "GreenwichUK", "HackneyUK", "HammersmithandFulhamUK", "HaringeyUK",
  "HarrowUK", "HaveringUK", "HillingdonUK", "HounslowCentralNorthandEastUK", "IslingtonEastUK", "IslingtonNorthUK", "IslingtonSouthUK",
  "IslingtonWestUK", "KensingtonandChelseaUK", "KingstonUK", "LambethUK", "LewishamUK", "LibraryUK", "MertonUK", "MuseumFreecycleUK",
  "NewhamUK", "RedbridgeUK", "RichmondUponThamesUK", "SouthwarkUK", "SuttonUK", "TowerHamletsUK", "WalthamForestUK", "WandsworthUK",
  "WestminsterUK"
];

// {group: id}
const lastIdPerGroup = (() => {
  const out = {}
  groups.forEach((g) => {
    out[g] = 0
  })
  return out
})()

// @return Promise
const getHtmlFromUrl = (url) => {
  return new Promise((resolve, reject) => {
    request({
      method: "GET",
      url: url,
    }, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      resolve(body.replace(/\r?\n|\r/g, ''));
    })
  });
};

// @return Array<Object> of format {id: String, title: String}
const extractData = (html, group) => {
  const out = []
  const $ = cheerio.load(html);
  $("tr.candy1, tr.candy2").each((index, el) => {
    const $el = cheerio(el)
    const text = $el.text()
    const id = matchIdRe.exec(text)[0].slice(2, -1)
    const title = matchTitleRe.exec(text)[0].slice(1, -11).trim()
    const url = $el.find("a").first().attr("href")
    const img = `https://groups.freecycle.org/group/${group}/post_image/${id}`
    out.push({id, title, url, img})
  })
  return out
}

// @return String
const composeUrl = (group) => {
  return `https://groups.freecycle.org/group/${group}/posts/offer`
}

// @return int
const getLastId = (arr) => {
  return arr[0].id
}

const getNewData = (groupId, lastIds, results) => {
  return results.filter((result) => {
    return result.id > lastIds[groupId]
  })
}

// return Array
const filter = (arr, re) => {
  return arr.filter((a) => {
    return re.test(a.title)
  })
}

// @param fn - function which returns a Promise
const repeat = (fn, period) => {
  console.log("running scraper", new Date())
  const d = new Date()
  if (d.getHours() > 0 && d.getHours() <= 6) {
    console.log("Night time mode enabled. Sleeping!")
    setTimeout(() => {
      console.log("Night time mode disabled. Awakening!")
      repeat(fn, period)
    }, 6 * 60 * 60 * 1000) // do it again in 6 hours.
    return
  }
  fn().then(() => {
    console.log("scraper finished", new Date())
    setTimeout(() => {
      repeat(fn, period)
    }, period)
  })
}

// @return Promise which resolves to an array of new items
const scraper = (lastIds) => {
  return Promise.all(groups.map((group) => {
    const url = composeUrl(group)
    return getHtmlFromUrl(url).then((body) => {
      const data = extractData(body, group)
      const filtered = filter(data, matchBikeRe)
      const newData = getNewData(group, lastIds, filtered)
      if (newData.length > 0) {
        lastIds[group] = getLastId(newData)
      }
      return Promise.resolve(newData)
    }, (err) => {
      console.error("Failed to fetch html for url", url, err)
    })
  }));
}

// return Promise
const scraperWithAlert = () => {
  return scraper(lastIdPerGroup).then((arrays) => {
    const joined = [].concat.apply([], arrays)
    if (joined.length > 0) {
      return sendAlert(joined)
    }
    return Promise.resolve()
  })
}

// @return String
const template = (data) => {
  let out = ""
  data.forEach((d) => {
    out += `
    <p><a href="${d.url}">${d.title}</a></p>
    <img src="${d.img}"/>
    `
  })
  return out
}

// @return Promise
const sendAlert = (data) => {
  return new Promise((resolve, reject) => {
    request({
      method: "POST",
      url: "https://api.mailgun.net/v3/sandbox1804b2f1d25f4a089c87b5e88d45a01e.mailgun.org/messages",
      auth: {
        user: "api",
        pass: "key-681aa043e91d821c0a5b04315f1b1a11",
      },
      form: {
        from: "postmaster@sandbox1804b2f1d25f4a089c87b5e88d45a01e.mailgun.org",
        to: ["alexandru.topliceanu@gmail.com", "simona.sorlescu@gmail.com"],
        subject: `FREECYCLE: bikes!`,
        text: JSON.stringify(data, null, "  "),
        html: template(data),
      },
    }, (err, res, body) => {
      if (err) {
        console.error("failed to send email to mailgun", err)
      } else {
        console.log("successfully sent emails", body)
      }
      resolve()
    })
  })
}

// run the scraper.
repeat(scraperWithAlert, SCRAPING_INTERVAL)

// run the api server ?!
const app = express()

app.set('port', (process.env.PORT || 5000));

app.get('/', function (req, res) {
  res.send('Hello Freecycle!')
})

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});
