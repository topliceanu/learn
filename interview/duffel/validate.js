const Joi = require('@hapi/joi');

exports.hello = Joi.object({
  name: Joi.string().required().min(1),
});

exports.search = Joi.object({
  sortBy: Joi.string().enum('price', 'duration'),
  order: Joi.string().enum('asc', 'desc').default('asc')
  origin: Joi.string().length(3).required(),
  destination: Joi.string().length(3).required(),
  departureDate: Joi.string().date(), // TODO ISO
})
