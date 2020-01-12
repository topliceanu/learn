<template>
  <div>
    <h2>Recent messages</h2>
    <ul>
      <li v-for="(message, index) in messages" v-bind:key="index">
        {{message.timestamp}}: {{ message.username }} says {{message.body}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'MessageList',
  data () {
    return {
      messages: this.$store.state.messages,
    }
  },
}
</script>
