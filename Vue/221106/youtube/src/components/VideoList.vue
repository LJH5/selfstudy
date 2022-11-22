<template>
  <div>
    <ul>
      <VideoListItem v-for="(video, index) in videos" :key="index"
      :video="video" @play="play"/>
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
    play: function (video) {      
      this.$emit('play', video)
    }
  }

}
</script>

<style>

</style>