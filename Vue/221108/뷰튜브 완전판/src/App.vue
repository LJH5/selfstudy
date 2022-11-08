<template>
  <div class="vuetube-wrap">
    <div class="container">
      <nav>
        <div class="d-flex justify-content-center">
          <h1 class="mt-3 text-primary">SSAFY TUBE</h1>
        </div>
        <SearchBar @fetch-videos="onFetchVideos"/>
      </nav>
      <section class="row">
        <div class="col-12 col-lg-8">
          <VideoDetail v-if="isSelectedVideo" :selectedVideo="selectedVideo"/>
          <div v-else class="unselected">
            <div class="img-area">
              <div>
                <img src="./assets/noResult.png" alt="noResult">
              </div>
              <p class="mt-4">선택된 비디오가 없습니다!</p>
              <p>비디오를 검색 하시거나 리스트에서 골라 주세요!</p>
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4">
          <VideoList :videos="videos" @select="onSelect"/>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

const URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'App',
  components: {
    SearchBar, VideoList, VideoDetail,
  },
  created() {
        axios.get(URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: '코딩노래',
        }
      })
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err => console.error(err))
  },
  data() {
    return {
      videos: [],
      selectedVideo: {},
    }
  },
  methods: {
    onFetchVideos(videos) {
      this.videos = videos
    },
    onSelect(selectedVideo) {
      this.selectedVideo = selectedVideo
    }
  },
  computed: {
    isSelectedVideo() {
      return !!Object.keys(this.selectedVideo).length
    }
  }

}
</script>

<style>
  .vuetube-wrap {
    min-height: 100vh;
  }

  h1 {
    font-weight: bold;
  }

  * {
    font-family: 'Noto Sans KR', sans-serif;
    color: rgb(88, 88, 88);
  }

  .unselected {
    height: 50vh;
    background-color: white;
    box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .img-area {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: large;
    font-weight: bold;
  }

  .img-area img {
    width: 200px;
  }
</style>