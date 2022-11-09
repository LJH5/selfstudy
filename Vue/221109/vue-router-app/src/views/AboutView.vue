<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{ name: 'home' }">홈으로 link</router-link>
    <button @click="toHome">홈으로 methods</button>
    <input type="text" @keyup.enter="toHello" v-model="inputData">
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null
    }
  },
  methods: {
    toHome() {
      this.$router.push({name: 'home'})
    },
    toHello() {
      this.$router.push({name: 'hello', params: { userName: this.inputData }})
    },
  }
}
</script>2