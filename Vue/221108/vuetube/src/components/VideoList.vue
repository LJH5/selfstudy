<template>
  <div>
    <ul class="list-group">
      <VideoListItem v-for="video in videos" 
        :key="video.etag"
        :video="video"
        @select="onSelect"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onSelect(selectedVideo) {
      // console.log(selectedVideo)
      this.$emit('select', selectedVideo)
    }
  }
}
</script>

<style>

</style>