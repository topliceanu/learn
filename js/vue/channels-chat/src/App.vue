<template>
  <div id="app">
    <h1>Channels Chat</h1>
    <p>logged in as {{username}}</p>
    <MessageList/>
    <NewMessage/>
  </div>
</template>

<script>
import MessageList from './components/MessageList.vue'
import NewMessage from './components/NewMessage.vue'

export default {
  name: 'app',
  components: {
    MessageList,
    NewMessage
  },
  data () {
    return {
      username: this.$store.state.username,
    }
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
