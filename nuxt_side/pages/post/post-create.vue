<template>
  <div class="container">
    <h1 class="title">
      Create Post
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subheader>Title</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-text-field v-model="postData.title" label="Title" 
          :rules="[required('title')]"
             />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Description</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-textarea v-model="postData.description" label="Description" 
          :rules="[required('description')]"
        type="text" />
        </v-col>
      </v-row>
      
      <v-btn name="submit-btn" @click="confirmPost">Confirm</v-btn>
      <v-btn name="submit-btn" @click="clearData">Clear</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  // name: 'IndexPage',
  data() {
    return {
      postData: {
        title: '',
        description: ''
      },
      valid: false,
      ...validations
    }
  },
  methods: {
    confirmPost() {
      this.$router.push({path: '/post/post-confirm'});
      if(this.postData.title && this.postData.description) {
        this.$store.commit('ADD_POST', this.postData)
      }
      
    },
    clearData() {
      this.postData.title = '';
      this.postData.description = '';
    }
  }
}
</script>

<style>
h1 {
  margin-bottom: 100px;
}
</style>