<template>
    <Base>
        <template #page_content>
            <div class="q-pa-md">
                <q-btn
                    label="Go back"
                    color="secondary"
                    text-color="dark"
                    type="a"
                    :href="backUrl"
                />
            </div>
            <div
                class="row q-col-gutter-md q-mb-xl"
                :class="{
                    'q-px-xl': $q.screen.gt.xs,
                    'q-px-md': $q.screen.lt.sm,
                }"
            >
                <div class="col-xs-12 col-md-9">
                    <div class="">
                        <section>
                            <h1 class="text-h1 text-capitalize">
                                {{ post.title }}
                            </h1>
                        </section>

                        <section>
                            <div>
                                <q-img
                                    :height="
                                        $q.screen.gt.xs ? '450px' : '300px'
                                    "
                                    :src="post.image"
                                />
                            </div>
                            <q-separator spaced="16px" />
                            <div class="row q-gutter-md">
                                <q-avatar class="">
                                    <img
                                        src="https://cdn.quasar.dev/img/avatar.png"
                                    />
                                </q-avatar>
                                <div>
                                    <div class="text-body1">
                                        {{ post?.author?.username }}
                                    </div>
                                    <div class="text-caption text-grey-7">
                                        {{ date_created }}
                                    </div>
                                </div>
                            </div>
                            <q-separator spaced="16px" />
                        </section>

                        <section v-html="post.body"></section>
                    </div>
                    <q-separator spaced="16px" />
                    <section>
                        <div class="text-h6 q-mb-md">Tags:</div>
                        <div class="q-gutter-sm">
                            <a
                                :href="tag.url"
                                v-for="tag in tags"
                                :key="tag.id"
                            >
                                <q-badge color="accent">
                                    #{{ tag.name }}
                                </q-badge>
                            </a>
                        </div>
                    </section>
                    <q-separator spaced="16px" />
                    <section v-if="post?.id">
                        <comments :authUser="authUser" :post_id="post_id" />
                    </section>
                    <q-separator spaced="16px" />

                    <!-- <div> -->
                    <!-- <section>
                        <related />
                    </section> -->
                    <!-- </div> -->
                </div>
                <div class="col-xs-12 col-md-3">
                    <div class="side_bar">
                        <sidebar :authUser="authUser" />
                    </div>
                </div>
                <!-- <div class=""> -->
                <section>
                    <related />
                </section>
                <!-- </div> -->
            </div>
        </template>
    </Base>
</template>

<script setup>
import Base from "../../components/layouts/Base.vue";
import Related from "../../components/blog/Related.vue";
import Sidebar from "../../components/blog/Sidebar.vue";
import getPostDetail from "../../composables/getPostDetail";
// import getComments from "../../composables/getComments";
import Comments from "../../components/blog/Comments.vue";
import { inject, onBeforeMount, provide, ref, watch } from "@vue/runtime-core";
import { date, useMeta } from "quasar";
import getAuthUser from "../../composables/getAuthUser";

const { callPostDetail, post, tags } = getPostDetail();
// const { callComments, comments } = getComments();
const { callAuthUser } = getAuthUser();

const user_is_authenticated = inject("user_is_authenticated");
const authUser = ref({});
onBeforeMount(async () => {
    await callPostDetail();
    if (user_is_authenticated) {
        authUser.value = await callAuthUser();
    }
});

const date_created = ref("");
const date_format = ref("");
const backUrl = document.referrer;
const post_id = ref(0);
const title = ref("");

watch(post, () => {
    if (post.value) {
        if (post.value.created_at) {
            date_format.value = new Date(post.value.created_at);

            date_created.value = date.formatDate(
                date_format.value,
                "MMMM Do, YYYY"
            );
        }
        // callComments(post.value.id);
        post_id.value = post.value.id;

        // title.value = post.value.title;
        title.value = `${post.value.title
            .charAt(0)
            .toUpperCase()}${post.value.title.slice(1)}`;
    }
});

// console.log(import.meta.env);

const metaData = () => ({
    // sets document title

    title: title.value,
    // optional; sets final title as "Index Page - ${import.meta.env.VITE_WEBSITE_NAME}", useful for multiple level meta
    titleTemplate: (title) => `${title} - ${import.meta.env.VITE_WEBSITE_NAME}`,

    // meta tags
    meta: {
        description: {
            name: "description",
            content: "Blog Website landing page. Latest news here",
        },
        keywords: {
            name: "keywords",
            content: "Quasar website blog django articles",
        },
        equiv: {
            "http-equiv": "Content-Type",
            content: "text/html; charset=UTF-8",
        },
        // note: for Open Graph type metadata you will need to use SSR, to ensure page is rendered by the server
        ogTitle: {
            property: "og:title",
            // optional; similar to titleTemplate, but allows templating with other meta properties
            template(ogTitle) {
                return `${ogTitle} - ${import.meta.env.VITE_WEBSITE_NAME}`;
            },
        },
    },
    // <noscript> tags
    noscript: {
        default: "This is content for browsers with no JS (or disabled JS)",
    },
});

useMeta(metaData);
</script>

<style lang="sass">
// .blog_image
//     height: 100px

//     @media (min-width: $breakpoint-sm-min)
//         height: 450px
</style>