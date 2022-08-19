<template>
    <div>
        <!-- <v-app-bar >
            <v-btn text to="/">Bulletin Board</v-btn>
        </v-app-bar> -->
        <nav>
            <ul>
                <li>
                    <NuxtLink to="/">Bulletin Board</NuxtLink>
                </li>

                <li>
                    <NuxtLink to="/">Home</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/post">Posts</NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/post/">Users</NuxtLink>
                </li>
            </ul>
        </nav>
        <main>
            <Nuxt />
        </main>
    </div>
</template>

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
    background-color: darkcyan;
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

main {
    margin: 0 auto;
    margin-top: 50px;
    padding: 0 1rem;
    max-width: 1280px;
    text-align: center;
}

img {
    margin-bottom: 1rem;
}

ul {
    list-style-type: none;
    padding: 15px 60px;
    display: flex;
    justify-content: left;
    flex-wrap: wrap;
    background-color: antiquewhite;
}

li {
    margin: 0 0.5rem;
    padding: 0.6rem;
    /* font-size: 1.2rem; */
}

nav {
    /* padding: 0 1rem; */
}

a.nuxt-link-exact-active {
    color: #00c58e;
}
</style>
