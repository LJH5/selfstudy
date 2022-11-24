<template>
  <div id="app">
    <TheSearchBar @search="search"/>
    <br><br><br>
    <VideoDetail :videoId="videoId"/>
    <ul>
      <VideoList :videos="videos" @play="play"/>
    </ul>
        
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      videos: [],
      video: {
      },
      videoId: '',
      BaseUrl: "https://www.googleapis.com/youtube/v3/search?key=AIzaSyCjUbWgGyVgvYblwhnVheJ1Lc687S_a0FU&part=snippet&type=video&q=",
    }
  },
  methods: {
    search: function (searched) {
      this.videos = []
      axios.get(this.BaseUrl+searched)
      .then((response) => {
        response.data.items.forEach(element => {
          this.videos.push(element)
        })
      })
    },
    play: function (video) {
      this.video = video
      this.videoId = this.video.id.videoId
      console.log(this.video.snippet.title)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
