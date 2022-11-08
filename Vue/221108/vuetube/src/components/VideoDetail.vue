<template>
  <div>
    <div class="ratio ratio-16x9">
      <iframe :src="`https://www.youtube.com/embed/${this.selectedVideo.id.videoId}`" frameborder="0"></iframe>
    </div>
    <div>
      <h4 class="mt-3">{{ selectedVideo.snippet.title }}</h4>
      <p>{{ selectedVideo.snippet.description}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: Object,
  },
  computed: {
  },
  methods: {
  }
}
</script>

<style>

</style>