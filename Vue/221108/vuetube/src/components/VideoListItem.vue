<template>
  <div>
    <li class="list-group-item video-item" @click="pickOne">
      <img class="rounded-4" :src="videoImgUrl" alt="thumbnail">
      <div class="mx-2 my-1">
        <div class="fs-5">{{ video.snippet.title }}</div>
        <p>{{ video.snippet.description }}</p>
      </div>
    </li>
  </div>
</template>

<script>

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoImgUrl() {
      return this.video.snippet.thumbnails.medium.url
    }
  },
  methods: {
    pickOne() {
      this.$emit('select', this.video)
    }
  }
}
</script>

<style>
  .video-item{
    display: flex;
    cursor: pointer;
  }
  .video-item:hover {
    background-color: rgba(255, 209, 236, 0.459);
  }

</style>