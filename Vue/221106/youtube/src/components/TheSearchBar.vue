<template>
  <div>
    <input 
      type="text"
      v-model="searched"
      @keyup.enter="search"
    >
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  data: function () {
    return {
      searched: null,
    }
  },
  methods: {
    search: function () {
      this.$emit('search', this.searched)
      this.searched = null
    }
  }

}
</script>

<style>

</style>