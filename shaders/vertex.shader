#version 330
in layout(location = 0) vec3 position;
in layout(location = 1) vec2 texture_cords;
in layout(location = 2) vec3 offset;
uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;
out vec2 textures;
void main()
{
    vec3 final_pos = vec3(position.x + offset.x, position.y + offset.y, position.z + offset.z);
    gl_Position =  proj * view * model * vec4(final_pos, 1.0f);
    textures = texture_cords;
}
