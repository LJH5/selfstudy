<template>
  <div>
    <ul class="list-group">
    <VideoListItem 
      v-for="video in videos"
      :key="video.etag"
      :video="video"
    />
  </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
 name: 'VideoList',
 components: {
  VideoListItem,
 },
 computed: {
  videos() {
    return this.$store.state.videos
  }
 }
}
</script>

<style>

</style>