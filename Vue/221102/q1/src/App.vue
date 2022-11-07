<template>
  <div id="app">
    <TheLunch :msg="msg" @pick-one-lunch-menu="pickOneInLunchMenu"/>
    <p>오늘의 메뉴는 {{ menu }} </p>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'


export default {
  name: 'App',
  components: {
    TheLunch
  },
  data: function () {
    return{
      msg: '점심메뉴',
      menu: '',
    }
  },
  methods: {
    pickOneInLunchMenu: function (pick) {
      this.menu = pick
    }
  }
}
</script>

<style>

</style>