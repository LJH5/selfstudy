<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article?.title }}</p>
    <p>내용: {{ article?.content }}</p>
    <p>작성시간: {{ article?.createdAt }}</p>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
  methods: {
    getArticleById(id) {
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      

    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>