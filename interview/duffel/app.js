const express = require('express');

const validate = require('./validate');

app = express();
app.use(express.json({ strict: false, type: '*/*' }));

app.post('/hello', (req, res) => {
  const output = validate.hello.validate(req.body)
  if (output.error) {
    res.status(400).json({ error: output.error });
    return
  }
  res.status(200).json({ 'hello': output.value.name });
})

app.post('/search', async (req, res) => {
  const input = {
    sortBy: req.query.sort_by,
    order: req.query.order,
    origin: req.body.origin,
    destination: req.body.destination,
    departureDate: req.body.departure_date,
  }
  const validated = validate.search.validate(input); // {value, error}
  if (validated.error) {
    res.status(400).json({ error: validated.error });
    return
  }
  try {
    const results = await api.search(validated.value)
    res.status(200).json({
      meta: {},
      flights: results,
    })
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
})

/* POST /search?sort_by=<field>&order=<asc|desc>
 *
 * sort_by - ...
 * order - defaults to asc
 *
 * request body:
 *  destination: string, length(3), required
 *  origin: string, length(3), required
 *  departure_date: date(iso8601), required
 *
 * returning:
 * {
 *  meta: {
 *   ....
 *  },
 *  flights: [{
 *    arrival_timestamp:
 *    departure_timestamp:
 *    duration_min:
 *    airline: a|b
 *    flight_id:
 *    flight_number:
 *    origin:
 *    destination:
 *    atomic_price:
 *    currency:
 *  }]
 * }
*/

module.exports = app;
