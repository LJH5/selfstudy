<template>
  <div class="lotto">
    <h1>로또</h1>
    <button @click="getNumber">Get Lucky Numbers</button>
    <p v-if="lottoNumbersLength">{{ lottoNumbers }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLottoView',
  data() {
    return {
      lottoNumbers: [],
      lottoNumbersLength: 0
    }
  },
  methods: {
    getNumber() {
      const nums = _.range(1, 46)
      this.lottoNumbers = _.sampleSize(nums, 6)
      this.lottoNumbersLength = this.lottoNumbers.length
    }
  },
}
</script>