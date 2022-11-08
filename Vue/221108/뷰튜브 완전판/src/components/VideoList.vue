<template>
  <ul class="list-group">
    <VideoListItem 
      v-for="video in videos"
      :key="video.etag"
      :video="video"
      @select="onSelect"
    />
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: { VideoListItem, },
  props: {
    videos: Array,
  },
  methods: {
    onSelect(selectedVideo) {
      this.$emit('select', selectedVideo)
    }
  }
}
</script>

<style>

</style>