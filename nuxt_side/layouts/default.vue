<template>
    <v-app>
        <v-app-bar app color="green">
            <v-toolbar-title>Bulletin Board</v-toolbar-title>
            <v-btn v-if="$auth.loggedIn" text to="/post">Posts</v-btn>
            <v-btn v-if="$auth.loggedIn" text to="/">Users</v-btn>
            <v-spacer />
            <div v-if="$auth.loggedIn">
                {{ $auth.user.email }}
                <v-btn text to="/" @click="$auth.logout()">Logout</v-btn>
            </div>
            <div v-else>
                <v-btn text to="/">Login</v-btn>
                <v-btn text to="/register">Register</v-btn>
            </div>
        </v-app-bar>
        <main>
            <Nuxt />
        </main>
    </v-app>
</template>
<script>
export default {
}
</script>
<style>
:root {
    --primary-color: #00c58e;
    font-size: 0.9em;
}

body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
        Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
        Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    margin: 0;
    padding: 0;
}

a {
    color: inherit;
    text-decoration: none;
}

nav a:hover {
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

v-app {
    margin: 0 auto;

    padding: 0 1rem;
    max-width: 1280px;
}

main {
    padding-top: 100px;
    background-color: rgb(186, 248, 218);
    text-align: center;
    height: 100%;
}

a.v-btn, .v-toolbar__title {
    margin-left: 25px;
}

a.nuxt-link-exact-active {
    color: #00c58e;
}
</style>
