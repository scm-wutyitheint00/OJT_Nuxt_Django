<template>
  <div class="container">
    <h1 class="title">
      Login Form
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subheader>Email</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-text-field v-model="loginInfo.email" label="Email" :rules="[required('email'), emailFormat()]"
            :class="{ 'my-text-style': loginInfo.email.someBool }" />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Password</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-text-field v-model="loginInfo.password" label="Password" :rules="[required('email'), minLenght('password', 8)]"
        type="password" />
        </v-col>
      </v-row>
      
      <v-btn name="submit-btn" @click="loginUser">Login</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  // name: 'IndexPage',
  data() {
    return {
      loginInfo: {
        email: '',
        password: ''
      },
      valid: false,
      ...validations
    }
  },
  methods: {
    loginUser() {
      this.$router.push('/user/post_create');
    }
  }
}
</script>

