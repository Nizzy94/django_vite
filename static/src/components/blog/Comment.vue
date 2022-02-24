
<script setup>
import { computed, toRefs } from "@vue/reactivity";
import ChildComment from "./ChildComment.vue";

// name: "comment";

const props = defineProps({
    comment: Object /** @type {Comment} */,
});

const { comment } = toRefs(props);
</script>

<template>
    <!-- <component :is="tag"> -->
    <q-item>
        <q-card flat class="comment-card" square>
            <q-card-section>
                <div class="text-caption text-grey-7">
                    <strong>{{ comment.user.username }}</strong> &bull; 5 min
                    ago
                </div>
            </q-card-section>

            <q-card-section class="q-pt-none">
                {{ comment.body }}
            </q-card-section>

            <q-card-actions>
                <q-btn label="Reply" flat size="sm" color="primary" />
            </q-card-actions>
            <q-card-section v-if="comment?.children?.length > 0">
                <q-list separator bordered class="comment-child-list">
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