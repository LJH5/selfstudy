import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videos: [],
    selectedVideo: {},
  },
  getters: {
  },
  mutations: {
    FETCH_VIDEOS(state, searchVideos){
      state.videos = searchVideos
    },
    SELECT(state, selectedVideo) {
      state.selectedVideo = selectedVideo
    }
  },
  actions: {
    fetchVideos(context, searchVideos) {
      // console.log(context)
      // console.log(searchVideo)
      context.commit('FETCH_VIDEOS', searchVideos)
    },
    select(context, selectedVideo) {
      context.commit('SELECT', selectedVideo)
    }
  },
  modules: {
  }
})
