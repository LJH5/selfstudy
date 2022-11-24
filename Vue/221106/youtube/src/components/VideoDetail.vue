<template>
  <div id='VideoDetail'>
    <iframe width="560" height="315" :src="src" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    videoId: String,
  },
  computed: {
    src() {
      return `https://www.youtube.com/embed/${this.videoId}`
    }
  }
}
</script>

<style>

</style>