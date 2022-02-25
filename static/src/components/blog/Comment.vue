
<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import ChildComment from "./ChildComment.vue";
import CommentForm from "./CommentForm.vue";

// name: "comment";

const props = defineProps({
    comment: Object,
    post_id: Number,
});

const { comment, post_id } = toRefs(props);

const user_is_authenticated = inject("user_is_authenticated");

const showReplyForm = ref(false);
</script>

<template>
    <!-- <component :is="tag"> -->
    <q-item>
        <q-card flat class="comment-card full-width q-mb-lg" square>
            <q-card-section>
                <div class="text-caption text-grey-7">
                    <strong>{{ comment.user.username }}</strong> &bull; 5 min
                    ago
                </div>
            </q-card-section>

            <q-card-section class="q-pt-none">
                {{ comment.body }}
            </q-card-section>

            <q-card-actions v-if="user_is_authenticated">
                <q-btn
                    :label="!showReplyForm ? 'Reply' : 'close'"
                    flat
                    size="sm"
                    @click="showReplyForm = !showReplyForm"
                    color="primary"
                />
            </q-card-actions>
            <q-card-section v-if="showReplyForm">
                <comment-form
                    :blog="post_id"
                    :is_parent="false"
                    :parent="comment?.id"
                />
            </q-card-section>
            <q-card-section v-if="comment?.children?.length > 0">
                <q-list separator bordered class="comment-child-list q-pl-lg">
                    <!-- <q-item v-for="comment in comments"> -->
                    <child-comment
                        :childComment="child"
                        v-for="child in comment.children"
                    />
                    <!-- </q-item> -->
                </q-list>
            </q-card-section>
        </q-card>
    </q-item>
</template>


<style lang="sass">
.comment-card
    border-left: 2px solid $grey-4

    .comment-child-list
        border-left: none
        border-right: none
        font-size: 12px
</style>