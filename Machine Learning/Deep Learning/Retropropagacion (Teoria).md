# Backpropagation

La retropropagación (backpropagation en inglés) es un algoritmo utilizado en el entrenamiento de redes neuronales artificiales en el campo del aprendizaje automático y la inteligencia artificial. Su función principal es ajustar los pesos de las conexiones entre neuronas para minimizar la diferencia entre las salidas deseadas y las salidas reales de la red.

Aquí hay una descripción básica del proceso de retropropagación:

1. **Paso hacia adelante (Forward Pass):**
   - La red neuronal recibe una entrada y realiza una serie de cálculos a través de sus capas ocultas para generar una salida.
   - Las salidas se comparan con las salidas deseadas para calcular el error.

2. **Cálculo del Error:**
   - Se calcula la diferencia entre las salidas reales y las salidas deseadas utilizando una función de pérdida (loss function).

3. **Retropropagación (Backward Pass):**
   - Se propaga el error hacia atrás a través de la red. Se calcula la derivada parcial del error con respecto a cada peso en la red.
   - Utilizando el gradiente descendente, los pesos de la red se actualizan de manera que el error se minimice. Esto implica ajustar los pesos en la dirección opuesta al gradiente de la función de pérdida.

4. **Iteración:**
   - El proceso de paso hacia adelante, cálculo del error, retropropagación y actualización de pesos se repite iterativamente a lo largo de varias épocas hasta que la red neuronal converge y los pesos alcanzan valores que minimizan la función de pérdida.

La retropropagación es esencial para el aprendizaje supervisado en redes neuronales. Permite que la red "aprenda" a través de la corrección de sus pesos en función de los errores cometidos durante la predicción de las salidas deseadas. Este proceso iterativo de ajuste de pesos es fundamental para que la red neuronal mejore su rendimiento en tareas específicas a lo largo del tiempo.

---

### ¿Como se calcula la retropropagación?

El cálculo de la retropropagación implica derivadas parciales y el uso del algoritmo de gradiente descendente para ajustar los pesos de la red neuronal y minimizar la función de pérdida. A continuación, se proporciona una descripción más detallada del proceso:

1. **Paso hacia adelante (Forward Pass):**
   - Proporciona una entrada a la red y realiza cálculos a través de cada capa hasta obtener una salida.

2. **Cálculo del Error:**
   - Calcula la diferencia entre la salida predicha y la salida deseada utilizando una función de pérdida. La función de pérdida mide qué tan bien está haciendo la red en la tarea que se le asignó.

3. **Retropropagación (Backward Pass):**
   - Calcula la derivada parcial del error con respecto a cada peso en la red utilizando la regla de la cadena y la propagación hacia atrás.
   - Se actualizan los pesos utilizando el algoritmo de gradiente descendente. La actualización de cada peso se realiza restando la tasa de aprendizaje (un hiperparámetro que controla el tamaño de los pasos en la dirección del gradiente) multiplicada por la derivada parcial del error con respecto a ese peso.

4. **Iteración:**
   - Se repiten los pasos 1-3 para varios ejemplos de entrenamiento y durante varias épocas hasta que la red converja y los pesos alcancen valores que minimicen la función de pérdida.

Para ilustrar el cálculo de la retropropagación, consideremos un caso simple con una red neuronal de dos capas (entrada y salida). Supongamos que tenemos una función de pérdida cuadrática como la función de pérdida:

$$ L(y, \hat{y}) = \frac{1}{2}(y - \hat{y})^2 $$

donde $y$ es la salida deseada y $\hat{y}$ es la salida predicha por la red. La derivada parcial del error con respecto a la salida predicha sería:

$$ \frac{\partial L}{\partial \hat{y}} = \hat{y} - y $$

Luego, usando esta derivada, se puede retropropagar el error a través de la red para calcular las derivadas parciales con respecto a los pesos y actualizar los pesos según el algoritmo de gradiente descendente. Este proceso se extiende a redes neuronales más complejas con múltiples capas y funciones de activación.

