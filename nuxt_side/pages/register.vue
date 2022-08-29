<template>
  <div class="register-page">
    <h1>Register Form</h1>
    <v-container>
      <v-layout align-center justify-center>
        <v-flex sm7>
          <v-form ref="form">
            <v-text-field v-model="userData.email" label="Enter your e-mail address" counter
              :rules="[required('email'), emailFormat()]"></v-text-field>
            <v-text-field v-model="userData.password" label="Enter your password"
              :rules="[required('password'), minLenght('password', 8)]" :append-icon="
                userData.showPassword ? 'mdi-eye' : 'mdi-eye-off'
              " :type="userData.showPassword ? 'text' : 'password'" @click:append="
  userData.showPassword = !userData.showPassword
"></v-text-field>
            <v-text-field v-model="userData.password2" label="Confirm password" :append-icon="
              userData.showPassword2 ? 'mdi-eye' : 'mdi-eye-off'
            " :type="userData.showPassword2 ? 'text' : 'password'"
              :rules="[required('confirm password'), minLenght('password', 8)]" @click:append="
                userData.showPassword2 = !userData.showPassword2
              "></v-text-field>
            <p class="red--text" v-if="!userData.valid">{{userData.error}}</p>
            <v-btn @click="signUp(userData)">
              Register
            </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  data: () => ({
    userData: {
      email: '',
      password: '',
      password2: '',
      showPassword: false,
      showPassword2: false,
      valid: true,
      error: null
    },
    ...validations
  }),
  methods: {
    async signUp(registrationInfo) {
      await this.$axios
        .$post('/customuser/', registrationInfo)
        .then((response) => {
          console.log('Successful');
          this.$router.push('/');
        })
        .catch((error) => {
          console.log('errors:', error.response.data.email)
          if(error.response.data.email) {
            this.userData.valid = false;
            this.userData.error = error.response.data.email[0];
          }
        })
    },
  },
}
</script>