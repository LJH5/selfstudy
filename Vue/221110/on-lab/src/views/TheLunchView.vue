<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <button @click="getMenu">Pick Lunch</button>
    <p>{{ menu }}</p><br>
    <h2>로또를 뽑아보자</h2>
    <button @click="toLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunchView',
  data() {
    return {
      menus: ['국밥', '짜장면', '햄버거'],
      menu: ''
    }
  },
  methods: {
    getMenu() {
      this.menu = _.sample(this.menus)
    },
    toLotto() {
      this.$router.push({ name: 'lotto'})
    }
  }
}
</script>
