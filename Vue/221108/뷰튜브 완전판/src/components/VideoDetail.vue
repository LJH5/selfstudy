<template>
  <div>
    <div class="ratio ratio-16x9">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
    <div class="detail">
      <h4>{{ videoTitle }}</h4>
      <p>{{ videoDescription }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: Object,
  },
  computed: {
    videoSrc() { return `https://youtube.com/embed/${this.selectedVideo.id.videoId}` },
    videoTitle() { return _.unescape(this.selectedVideo.snippet.title) },
    videoDescription() { return _.unescape(this.selectedVideo.snippet.description) }
  }
}
</script>

<style>
.detail {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 2px;
  background-color: white;
  box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}
</style>