<template>
  <div id="app" class="container vuetube-warp">
    <!-- 제목 영역 -->
    <header class="d-flex justify-content-center">
      <h1 class="mt-4 text-primary">VueTube</h1>
    </header> 
    <!-- 검색바 -->
    <SearchBar @fetch-vidoes="onFetchVideos"/>

    <!-- 본문 영역 -->
    <section class="row mt-4">
      <!--  비디오 플레이 영역 -->
      <article class="col-12">
        <VideoDetail :selectedVideo="selectedVideo"/>
      </article>
      <!-- 오른쪽에 보일 비디오 리스트 5개 -->
      <aside class="col-12">
        <VideoList :videos="videos" @select="onSelect"/>
      </aside>

    </section>

  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'

export default {
  name: 'App',
  components: {
    SearchBar, VideoDetail, VideoList,
  },
  data() {
    return{
      videos: [],
      selectedVideo: {},
    }
  },
  methods: {
    onFetchVideos(videos) {
      // console.log(videos)
      this.videos = videos
    },
    onSelect(selectedVideo) {
      this.selectedVideo = selectedVideo
    },
  }
}
</script>

<style>
  .vuetube-warp {
    min-height: 100vh;
  }
</style>
