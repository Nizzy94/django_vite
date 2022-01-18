<template>
    <Base>
        <template #page_content>
            <div
                class="q-mx-auto"
                :class="{
                    'q-px-sm': $q.screen.lt.md,
                }"
                style="max-width: 920px; width"
            >
                <section>
                    <h1 class="text-h4">
                        Asperiores, aliquam quidem molestias quod excepturi
                        alias dolorum corrupti quis suscipit ab.
                    </h1>
                </section>

                <section>
                    <div>
                        <q-img
                            height="400px"
                            src="https://cdn.quasar.dev/img/mountains.jpg"
                        />
                    </div>
                    <q-separator spaced="16px" />
                    <div class="row q-gutter-md">
                        <q-avatar class="">
                            <img src="https://cdn.quasar.dev/img/avatar.png" />
                        </q-avatar>
                        <div>
                            <div class="text-body1">Jane Doe</div>
                            <div class="text-caption text-grey-6">
                                Jan 23, 2001
                            </div>
                        </div>
                    </div>
                    <q-separator spaced="16px" />
                </section>

                <section>
                    <div>
                        <p class="text-body1">
                            Est aliqua aute sit culpa qui. Occaecat nisi ipsum
                            deserunt minim pariatur duis eiusmod proident irure
                            commodo. Do eiusmod et est mollit sint et ullamco
                            laboris officia nisi dolor Lorem. Adipisicing dolor
                            nisi ipsum minim adipisicing ipsum amet dolor.
                            Voluptate est elit dolor ut ad reprehenderit
                            occaecat esse ad commodo incididunt irure eu. Fugiat
                            deserunt sunt excepteur occaecat pariatur et
                            voluptate qui esse eu. Excepteur eu cillum pariatur
                            nostrud duis in minim ea reprehenderit mollit elit
                            aliquip.
                        </p>
                        <p class="text-body1">
                            Ut dolore culpa aliqua mollit pariatur ad nulla
                            excepteur labore enim. Laboris reprehenderit aute id
                            aute consectetur in cupidatat dolore in nisi in
                            adipisicing irure consectetur. Ut fugiat laboris
                            enim et eiusmod consequat nostrud nostrud. Commodo
                            eu tempor sunt fugiat. Ut sint adipisicing duis sit
                            labore velit. Ex sint id anim ipsum velit commodo ad
                            tempor nulla proident velit. Cupidatat aliquip sint
                            incididunt consequat irure esse cillum nisi
                            voluptate anim.
                        </p>
                        <p class="text-body1">
                            Proident ipsum esse quis id est excepteur. Ut
                            excepteur pariatur ipsum quis ad. Commodo amet
                            occaecat id occaecat mollit non aliqua. Pariatur
                            cupidatat eu adipisicing nostrud. Fugiat Lorem esse
                            exercitation laboris do Lorem nostrud aliquip ut
                            dolor ea sit nulla enim. Nulla qui magna ad duis id
                            duis deserunt est consequat qui reprehenderit eu
                            ullamco culpa. Excepteur nulla culpa consequat Lorem
                            cillum.
                        </p>
                        <p class="text-body1">
                            Sit veniam commodo sunt ea nisi ipsum. Velit do esse
                            aliquip velit incididunt. Eu eiusmod elit
                            consectetur velit incididunt Lorem non tempor eu
                            cupidatat velit dolore dolor veniam. Nisi officia
                            cillum sint enim do occaecat do magna irure
                            incididunt in.
                        </p>
                        <p class="text-body1">
                            Commodo dolor mollit in laboris eiusmod et aliqua
                            aliquip amet. Labore exercitation consectetur
                            deserunt exercitation excepteur culpa consequat enim
                            tempor proident. Commodo ea non ullamco irure fugiat
                            consectetur voluptate commodo anim deserunt
                            consectetur qui. Duis do non velit cillum non dolor
                            deserunt irure pariatur sit laboris pariatur cillum.
                        </p>
                        <p class="text-body1">
                            Eiusmod sunt ad mollit irure consectetur cupidatat
                            ex aliqua esse labore ex amet. Ipsum ex officia
                            cupidatat ut magna. Deserunt amet duis Lorem officia
                            id esse.
                        </p>
                    </div>
                </section>
            </div>
            <q-separator spaced="16px" />
            <div>
                <section>
                    <related />
                </section>
            </div>
        </template>
    </Base>
</template>

<script setup>
import Base from "../../components/layouts/Base.vue";
import Related from "../../components/blog/Related.vue";
</script>

<style>
</style>