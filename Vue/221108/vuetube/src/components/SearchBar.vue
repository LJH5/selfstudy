<template>
  <div class="search-box m-auto d-flex justify-content-center">
    <input class=" form-control rounded-0" type="text" @keyup.enter="onSearch" v-model="query">
    <button class="btn btn-primary rounded-0 w-25 fs-3" @click="onSearch">검색</button>
  </div>
</template>

<script>
import axios from 'axios'

const URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'SearchBar',
  data() {
    return {
      query: ''
    }
  },
  methods: {
    onSearch() {
      // console.log(this.query)
      axios.get(URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: this.query
        }
      })
      .then(res => this.$emit('fetch-vidoes', res.data.items))
      .catch()
    }
  }
}
</script>

<style>
  .search-box{
    max-width: 700px;
  }
</style>