const request = require('request');

const factory = (airlineId) => {
  switch(airlineID) {
    'a': return searchA; break;
    'b': return searchB; break;
  }
}

// @param {String} origin
// @param {String} destination
// @param {Date} departureDate
// @return {Array<Flight>}
//
/* Flight:
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
 *
 * TODO: retries,
 */
const searchA = async (origin, destination, departureDate) => {
  const res = await request(AIRLINE_A_SEARCH_URL, {
    Headers: {
      "Content-type": 'application/json'
    },
    Body: JSON.stringify({
      origin,
      destination,
      departure_date: departureDate,
    })
  })
  if (res.status !== 200) {
    throw new Error(`Failed to contact airline A with status ${res.status} and error ${err}`);
  }
  return res.body.data.offers.map((offer) => {
    return {
      arrival_timestamp:
      departure_timestamp:
      duration_min:
      airline: a|b
      flight_id:
      flight_number:
      origin:
      destination:
      atomic_price:
      currency:
    }
  })
}
