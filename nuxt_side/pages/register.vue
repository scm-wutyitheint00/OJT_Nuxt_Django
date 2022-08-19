<template>
  <div class="register-page">
    <h1>Register Form</h1>
    <v-container>
      <v-layout align-center justify-center>
        <v-flex sm7>
            <v-form ref="form">
                <v-text-field
                v-model="userData.email"
                label="Enter your e-mail address"
                counter
                :rules="[required('email'), emailFormat()]"
                ></v-text-field>
                <v-text-field
                v-model="userData.password"
                label="Enter your password"
                :rules="[required('password'), minLenght('password', 8)]"
                :append-icon="
                    userData.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                "
                :type="userData.showPassword ? 'text' : 'password'"
                @click:append="
                    userData.showPassword = !userData.showPassword
                "
                ></v-text-field>
                <v-text-field
                v-model="userData.password2"
                label="Confirm password"
                :append-icon="
                    userData.showPassword2 ? 'mdi-eye' : 'mdi-eye-off'
                "
                :type="userData.showPassword2 ? 'text' : 'password'"
                :rules="[required('confirm password'), minLenght('password', 8)]"
                @click:append="
                    userData.showPassword2 = !userData.showPassword2
                "
                ></v-text-field>
                <!-- <v-layout justify-space-between> -->
                <v-btn @click="signUp(userData)">
                    Register
                </v-btn>
                
                <!-- </v-layout> -->
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
          console.log('errors:', error.response)
        })
    //   this.$auth.loginWith('local', {
    //     data: registrationInfo,
    //   })
    },
  },
}
</script>