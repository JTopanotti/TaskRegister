<template>
  <div id="hour-field">
    <input type="time" v-model="before" style="margin-right: 5px">
    <input type="time" v-model="after" style="margin-right: 5px">
    <input type="time" v-model="time" disabled="true">
  </div>
</template>

<script>
export default {
  name: 'HourField',
  props: ['index', 'list'],
  components: {},
  data () {
    return {
      before: '08:00:00',
      after: '10:00:00'
    }
  },
  computed: {
    time: function() {
      let beforeDate = this.getDate(this.before)
      let afterDate = this.getDate(this.after)
      let delta = Math.abs(afterDate - beforeDate) / 1000
      let hours = Math.floor(delta / 3600) % 24
      delta -= hours * 3600
      let minutes = Math.floor(delta / 60) % 60
      let time = hours.toString().padStart(2, '0') + ":" + minutes.toString().padStart(2, '0')
      //BUG: when the hours is 00, the time input sets it to 12
      this.setTimeInList(time)
      return time
    }
  },
  methods: {
    getDate(str) {
      let date = new Date()
      date.setHours(str.substr(0, 2))
      date.setMinutes(str.substr(3, 2))
      date.setSeconds(0)
      return date
    },
    setTimeInList(time) {
      this.list[this.index] = time
    }
  }
}
</script>