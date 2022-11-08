<template>
  <div class="search-bar-div d-flex justify-content-center align-items-center">
    <input class="search-input" @input="onInput" @keyup.enter="onChange">
    <button class="btn btn-primary ms-2 search-btn" @click="onChange">검색</button>
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
      query: '',
    }
  },
  methods: {
    onInput(event) {
      this.query = event.target.value
    },
    onChange() {
      axios.get(URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: this.query,
        }
      })
        .then(res => this.$emit('fetch-videos', res.data.items))
        .catch(err => console.error(err))
    }
  }
}
</script>

<style>
.search-bar-div {
  text-align: center;
  margin: 20px;
}

.search-input {
  width: 50%;
  height: 40px;
  border: 1px solid rgb(13, 110, 253);
  border-radius: 4px;
  outline: none;
}

.search-btn {
  height: 40px !important;
}

</style>