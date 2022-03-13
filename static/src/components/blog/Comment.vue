
<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject, watch } from "@vue/runtime-core";
import ChildComment from "./ChildComment.vue";
import CommentForm from "./CommentForm.vue";

const props = defineProps({
    comment: Object,
    post_id: Number,
});

const { comment, post_id } = toRefs(props);

const user_is_authenticated = inject("user_is_authenticated");

// const comment_value = ref(comment.value.body);
const showReplyForm = ref(false);

const showEditform = ref(false);

const updateComment = async (res) => {
    console.log(res);
    showEditform.value = false;
    comment.value.body = res.body;
    comment.value.updated_at = res.updated_at;
    comment.value.edited = res.edited;

    // comment.value
};

const addComment = async (res) => {
    console.log(res);
    showReplyForm.value = false;

    comment.value.children.unshift(res);
};
</script>

<template>
    <!-- <component :is="tag"> -->
    <q-item>
        <q-card flat class="comment-card full-width q-mb-lg" square>
            <q-card-section>
                <div class="text-caption text-grey-7">
                    <strong>{{ comment.user.username }}</strong> &bull;
                    {{ comment.created_at }}
                    <span v-if="comment.edited">
                        &bull; <strong> Edited:</strong>
                        {{ comment.updated_at }}
                    </span>
                </div>
            </q-card-section>

            <q-card-section class="q-pt-none" v-if="showEditform">
                <!-- <q-input
                    v-model="comment_value"
                    autofocus
                    @blur="(evnt) => (showEditform = false)"
                    @keyup.enter="updateComment"
                /> -->
                <comment-form
                    :blog="post_id"
                    :value="comment.body"
                    @addComment="updateComment"
                    :isEditForm="true"
                    :comment_id="comment.id"
                />
            </q-card-section>
            <q-card-section class="q-pt-none" v-else>
                {{ comment.body }}
            </q-card-section>

            <q-card-actions v-if="user_is_authenticated">
                <div class="row">
                    <div>
                        <q-btn
                            :label="!showReplyForm ? 'Reply' : 'close'"
                            flat
                            size="sm"
                            @click="showReplyForm = !showReplyForm"
                            color="primary"
                        />
                    </div>
                    <div>
                        <q-btn
                            :label="'Edit'"
                            flat
                            icon="mdi-square-edit-outline"
                            size="sm"
                            @click="showEditform = !showEditform"
                            color="grey-6"
                        />
                        <q-btn
                            :label="'Delete'"
                            flat
                            icon="mdi-delete"
                            size="sm"
                            @click="showReplyForm = !showReplyForm"
                            color="grey-6"
                        />
                    </div>
                </div>
            </q-card-actions>
            <q-card-section v-if="showReplyForm">
                <comment-form
                    :blog="post_id"
                    :is_parent="false"
                    :parent="comment?.id"
                    @addComment="addComment"
                />
            </q-card-section>
            <q-card-section v-if="comment?.children?.length > 0">
                <q-list separator bordered class="comment-child-list q-pl-lg">
                    <!-- <q-item v-for="comment in comments"> -->
                    <child-comment
                        :childComment="child"
                        v-for="child in comment?.children"
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