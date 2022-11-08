<template>
  <div class="video-list-wrap">
    <li class="list-group-item video-item" @click="onClick">
      <img class="me-3" :src="videoImgUrl" alt="video-thumbnail">
      <div class="media-body">
        {{ video.snippet.title }}
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
  methods: {
    onClick() {
      this.$emit('select', this.video)
    }
  },
  computed: {
    videoImgUrl () {
      return this.video.snippet.thumbnails.default.url
    }
  }

}
</script>

<style>
  .video-item {
    display: flex;
    cursor: pointer;
  }

  .video-item:hover {
    background-color: #eee;
  }

  .video-list-wrap {
    box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  }
</style>