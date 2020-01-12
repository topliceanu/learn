import Vue from 'vue'
import Vuex from 'vuex'
import Pusher from 'pusher-js'

Vue.use(Vuex)

// Setup Pusher
const client = new Pusher("TODO", {
  cluster: 'eu',
  forceTLS: true,
  authEndpoint: "/auth",
})
const channel = client.subscribe("private-messages");

// Define the store
const store = new Vuex.Store({
  state: {
    username: `user-${Math.random().toString(36).substring(7)}`,
    messages: [],
  },
  mutations: {
    POST_NEW_MESSAGE (state, newMessage) {
      state.messages.push(newMessage)
    },
  },
  actions: {
    postNewMessage (context, newBody) {
      const newMessage = {
        username: this.state.username,
        body: newBody,
        timestamp: (new Date()).toLocaleString(),
      }
      channel.trigger('client-new-message', newMessage)
      context.commit('POST_NEW_MESSAGE', newMessage)
    },
    receivedNewMessage (context, newMessage) {
      context.commit('POST_NEW_MESSAGE', newMessage)
    },
  },
  getters: {
    // TODO filters for our state.
  },
})

channel.bind("new-message", (newMessage) => {
  store.dispatch('receivedNewMessage', newMessage)
})

export default store
