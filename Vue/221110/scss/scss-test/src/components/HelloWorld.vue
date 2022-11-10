<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="box">
      <span class="box_greeting">안녕?</span>
      <div class="box_child">
        <ul class="box_child_list">
          <li class="box_child_list_item">1</li>
          <li class="box_child_list_item">2</li>
          <li class="box_child_list_item">3</li>
        </ul>
      </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
