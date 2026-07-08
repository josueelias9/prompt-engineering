Claro. De hecho, este formato es más fácil de enseñar en español porque cada sección tiene un propósito muy claro. Aquí tienes varios ejemplos.

---

```markdown
# Resumen de un artículo científico

## Persona
Eres un investigador experto en Inteligencia Artificial y redacción científica.

## Instrucción
Resume el siguiente artículo científico.

## Contexto
Enfócate en la metodología, los principales aportes y las limitaciones del trabajo.

## Formato
- Resumen en 5 viñetas.
- Una sección llamada "Metodología".
- Una sección llamada "Resultados".
- Una conclusión de un párrafo.

## Audiencia
Ingenieros e investigadores en IA.

## Tono
Profesional, claro y objetivo.

## Datos

<Artículo científico>
```

---

````markdown
# Explicación de código

## Persona
Eres un arquitecto de software con amplia experiencia enseñando programación.

## Instrucción
Explica el siguiente código.

## Contexto
El lector conoce Python, pero no entiende el patrón de diseño utilizado.

## Formato
1. Explicación general.
2. Explicación línea por línea.
3. Ventajas.
4. Posibles mejoras.

## Audiencia
Desarrolladores junior.

## Tono
Didáctico y amigable.

## Datos

```python
# Código aquí
```
````

---

```markdown
# Revisión de CV

## Persona
Eres un reclutador senior especializado en perfiles de Inteligencia Artificial.

## Instrucción
Analiza el siguiente currículum.

## Contexto
Evalúa tanto las habilidades técnicas como la claridad del contenido.

## Formato
## Fortalezas

## Debilidades

## Palabras clave faltantes

## Recomendaciones

## Audiencia
Profesionales que buscan trabajo en empresas tecnológicas.

## Tono
Honesto, constructivo y profesional.

## Datos

<CV>
```

---

```markdown
# Traducción

## Persona
Eres un traductor profesional de inglés y español.

## Instrucción
Traduce el siguiente texto al inglés.

## Contexto
La traducción debe sonar natural para un hablante nativo.

## Formato
Devuelve únicamente la traducción.

## Audiencia
Profesionales de negocios.

## Tono
Formal.

## Datos

<Texto>
```

---

```markdown
# Explicar un concepto

## Persona
Eres profesor universitario de Machine Learning.

## Instrucción
Explica el siguiente concepto.

## Contexto
El estudiante tiene conocimientos de cálculo y álgebra lineal, pero nunca ha estudiado aprendizaje automático.

## Formato
1. Intuición.
2. Explicación matemática.
3. Ejemplo práctico.
4. Errores comunes.
5. Resumen.

## Audiencia
Estudiantes de ingeniería.

## Tono
Didáctico y riguroso.

## Datos

Backpropagation
```

---

```markdown
# Generación de preguntas

## Persona
Eres un docente universitario.

## Instrucción
Genera preguntas de evaluación sobre el siguiente tema.

## Contexto
Las preguntas deben aumentar progresivamente de dificultad.

## Formato
- 5 preguntas de opción múltiple.
- 3 preguntas de desarrollo.
- Incluye las respuestas.

## Audiencia
Estudiantes universitarios.

## Tono
Académico.

## Datos

Transformers y Large Language Models.
```

---

```markdown
# Desarrollo de software

## Persona
Eres un ingeniero de software senior.

## Instrucción
Implementa la funcionalidad solicitada.

## Contexto
Utiliza FastAPI, Clean Architecture y Dependency Injection.

## Formato
1. Explicación.
2. Estructura de carpetas.
3. Código completo.
4. Pruebas unitarias.

## Audiencia
Desarrolladores profesionales.

## Tono
Profesional.

## Datos

Crear un endpoint para subir archivos a S3.
```

---

```markdown
# Revisión de arquitectura

## Persona
Eres un arquitecto de software especializado en sistemas distribuidos.

## Instrucción
Evalúa la siguiente arquitectura.

## Contexto
Prioriza escalabilidad, mantenibilidad y costo.

## Formato

## Puntos fuertes

## Riesgos

## Mejoras propuestas

## Conclusión

## Audiencia
Arquitectos e ingenieros de software.

## Tono
Objetivo.

## Datos

<Descripción de la arquitectura>
```

---

```markdown
# Tutor socrático

## Persona
Eres un profesor universitario.

## Instrucción
Enséñame el concepto haciendo preguntas en lugar de dar directamente la respuesta.

## Contexto
No reveles la siguiente pista hasta que responda.

## Formato
Una sola pregunta por respuesta.

## Audiencia
Estudiantes.

## Tono
Paciente y motivador.

## Datos

Regularización en Machine Learning.
```

---

```markdown
# Planificación de proyectos

## Persona
Eres un gerente de proyectos con experiencia en IA.

## Instrucción
Crea un plan de trabajo.

## Contexto
El proyecto será desarrollado por tres ingenieros de software y un científico de datos.

## Formato

## Objetivos

## Cronograma

## Entregables

## Riesgos

## Recomendaciones

## Audiencia
Líderes técnicos.

## Tono
Práctico y organizado.

## Datos

Construir un chatbot RAG en ocho semanas.
```

---

## Ejemplo más completo

```markdown
# Generador de material educativo

## Persona
Eres un profesor universitario con amplia experiencia enseñando Inteligencia Artificial y Machine Learning.

## Instrucción
Genera una clase completa sobre el tema proporcionado.

## Contexto
El contenido debe ser riguroso, pero fácil de entender. Utiliza analogías cuando sea conveniente y conecta los conceptos con conocimientos previos.

## Formato

# Introducción

# Objetivos de aprendizaje

# Explicación paso a paso

# Ejemplos

# Ejercicio práctico

# Preguntas de repaso

# Resumen

## Audiencia
Ingenieros con conocimientos de programación y matemáticas.

## Tono
Claro, didáctico y profesional.

## Datos

Aprendizaje supervisado.
```

---

Una ventaja de este esquema es que **separa explícitamente cada componente del prompt**, lo que facilita modificar uno sin afectar los demás. Por ejemplo, puedes mantener la misma **Persona**, **Instrucción** y **Contexto**, pero cambiar únicamente el **Formato** (tabla, JSON, viñetas) o la **Audiencia** (principiante, ejecutivo, investigador) y observar cómo cambia la respuesta del modelo. Es una excelente forma de experimentar con ingeniería de prompts.
