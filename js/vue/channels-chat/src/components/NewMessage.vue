<template>
  <div>
    <h2>Post new message</h2>
    <form @submit.prevent="onSubmit">
      <input type="text" v-model="newBody"/>
      <input type="submit" value="Post"/>
    </form>
  </div>
</template>

<script>
export default {
  name: 'NewMessage',
  data () {
    return {
      newBody: null,
    }
  },
  methods: {
    onSubmit () {
      this.$store.dispatch('postNewMessage', this.newBody);
      this.newBody = null;
    }
  },
}
</script>
