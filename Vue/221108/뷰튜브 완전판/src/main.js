import Vue from 'vue'  // 내 위치에 vue 파일 찾기 => 없음 => node_modules 탐색
import App from './App.vue'  // 위치 명시 => 내 위치에서 찾기

new Vue({
  // render: function (createElement) { return createElement(App) }
  render: h => h(App)
}).$mount('#app')