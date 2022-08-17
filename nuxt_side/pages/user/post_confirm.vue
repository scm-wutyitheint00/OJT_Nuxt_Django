<template>
  <div class="container">
    <h1 class="title">
      Confirm Post
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subheader>Title</v-subheader>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle-2" value="this.confirmData.title">
            {{ $store.state.posts.title }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Description</v-subheader>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle-2" value="this.confirmData.description">
            {{ $store.state.posts.description }}
          </p>
        </v-col>
      </v-row>

      <v-btn name="submit-btn" @click="loginUser">Create</v-btn>
      <v-btn name="submit-btn" @click="clickCancel">Cancel</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {

  // name: 'IndexPage',
  data() {
    return {
      confirmData: {
        title: '',
        description: ''
      },
      valid: false,
      ...validations
    }
  },
  methods: {
    loginUser() {
      
    },
    clickCancel() {
      this.$router.push('/user/post_create');
    }
  }
}
</script>

<style>
h1 {
  margin-bottom: 100px;
}
</style>