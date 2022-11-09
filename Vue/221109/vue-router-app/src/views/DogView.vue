<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="강아지"><br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중..."
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
      .then((response) => {
        this.imgSrc = response.data.message
      })
      .catch((error) => {
        console.log(error)
        // this.message = `${this.$route.params.breed}는 없는 품종입니다.`
        this.$router.push('/404')
      })
    }
  },
  created() {
    this.getDogImage()
  }
}
</script>

<style>

</style>