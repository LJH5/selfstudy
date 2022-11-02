<template>
  <div>
    <h1>{{ msg }}</h1>
    <button @click="pickOneInLunchMenu">PickOne</button>
  </div>
</template>

<script>
export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch:['국밥', '짜장면', '햄버거'],
      selectLunchMenu: null,
      lunchIdx:[],
    }
  },
  props:{
    msg: String
  },
  methods:{
    pickOneInLunchMenu: function () {
      this.$emit('pick-one-lunch-menu', '국밥')
    }
  }
}
</script>

<style>

</style>