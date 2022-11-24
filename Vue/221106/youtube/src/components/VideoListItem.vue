<template>
  <li>
    <img :src="img" alt="">
    <h3 @click="play">{{ video.snippet.title }}</h3>
    <p>{{ video.snippet.channelTitle }}</p>
    <p>{{ video.snippet.description }}</p>
  <hr>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  data: function () {
    return {
      img: this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    play: function () {      
      this.$emit('play', this.video)
    }
  }

}
</script>

<style>

</style>