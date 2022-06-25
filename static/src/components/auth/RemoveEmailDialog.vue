<template>
    <q-dialog
        v-model="openConfirmDialog"
        transition-show="slide-down"
        transition-hide="slide-up"
    >
        <q-card style="min-width: 350px">
            <form :action="routes?.auth_routes?.account_email" method="post">
                <q-card-section>
                    <div class="text-h6">
                        Are you sure you want to remove
                        <strong>{{ selected_email }}</strong
                        >?
                    </div>
                    <!-- {{ selected_email }} -->
                    <input
                        name="email"
                        :value="selected_email"
                        type="radio"
                        checked
                        hidden
                    />
                    <input
                        name="csrfmiddlewaretoken"
                        type="hidden"
                        :value="$q.cookies.get('csrftoken')"
                    />
                </q-card-section>
                <q-separator spaced />

                <q-card-actions class="q-pt-md" align="around">
                    <!-- {{ user_is_authenticated }} -->

                    <!-- <div class="row justify-around"> -->
                    <!-- :href="`/login/auth/${redirect_query}`" -->
                    <q-btn
                        v-close-popup
                        color="primary"
                        outline
                        label="Cancel"
                    />
                    <q-btn
                        color="negative"
                        type="submit"
                        name="action_remove"
                        label="Remove"
                    />
                    <!-- </div> -->
                </q-card-actions>

                <!-- <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Search" v-close-popup />
        </q-card-actions> -->
            </form>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { ref, toRefs } from "@vue/reactivity";

const props = defineProps({
    selected_email: {
        type: String,
        required: true,
    },
    // openDialog: {
    //     type: Boolean,
    //     required: true,
    // },
    routes: {
        type: Object,
        required: true,
    },
});

const { selected_email, routes } = toRefs(props);

const openConfirmDialog = ref(false);
// const selected_email = ref();

defineExpose({ openConfirmDialog });
</script>

<style>
</style>