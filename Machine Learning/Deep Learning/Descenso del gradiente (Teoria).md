# Gradient Descent

El descenso del gradiente es un algoritmo de optimización utilizado en el entrenamiento de modelos en machine learning y deep learning, incluyendo redes neuronales. El objetivo del descenso del gradiente es minimizar una función de pérdida ajustando los parámetros del modelo. En el contexto de las redes neuronales, estos parámetros son los pesos de las conexiones entre las neuronas.

Aquí hay una descripción básica del descenso del gradiente:

1. **Inicialización:**
   - Se inician los pesos del modelo con valores aleatorios o predefinidos.

2. **Paso hacia adelante (Forward Pass):**
   - Se pasa una entrada a través del modelo para obtener una predicción.

3. **Cálculo de la Pérdida:**
   - Se calcula la diferencia entre la predicción del modelo y la salida deseada utilizando una función de pérdida.

4. **Paso hacia atrás (Backward Pass):**
   - Se calculan las derivadas parciales de la función de pérdida con respecto a los pesos de la red utilizando la retropropagación.
   - Estas derivadas indican la dirección y la magnitud del cambio que se debe hacer en cada peso para reducir la pérdida.

5. **Actualización de Pesos:**
   - Se actualizan los pesos en la dirección opuesta al gradiente de la función de pérdida.
   - La tasa de aprendizaje es un hiperparámetro que controla el tamaño de los pasos que se dan en esta dirección. Una tasa de aprendizaje demasiado pequeña puede llevar a convergencia lenta, mientras que una demasiado grande puede hacer que el modelo no converja o incluso diverja.

6. **Iteración:**
   - Se repiten los pasos anteriores para múltiples ejemplos de entrenamiento y durante varias épocas hasta que la función de pérdida converge a un valor mínimo o se detiene según algún criterio predefinido.

El descenso del gradiente busca encontrar el mínimo local (o global) de la función de pérdida al seguir la dirección de mayor descenso. En el contexto de las redes neuronales y deep learning, donde las funciones de pérdida y las arquitecturas de red pueden ser altamente no lineales y complejas, el descenso del gradiente se combina comúnmente con variantes como el descenso del gradiente estocástico (SGD) o el descenso del gradiente con momento para mejorar la eficiencia y superar posibles problemas de convergencia.

---

### Cálculo del descenso del gradiente

El cálculo del descenso del gradiente implica actualizar iterativamente los pesos de la red neuronal en la dirección opuesta al gradiente de la función de pérdida con respecto a esos pesos. A continuación, se proporciona una descripción paso a paso del cálculo del descenso del gradiente:

Supongamos que tenemos una red neuronal con parámetros $\theta$ (que representan los pesos y sesgos) y una función de pérdida $J(\theta)$ que queremos minimizar.

1. **Inicialización:**
   - Se inician los pesos $\theta$ con valores aleatorios o predefinidos.

2. **Paso hacia adelante (Forward Pass):**
   - Se realiza un pase hacia adelante en la red neuronal utilizando la entrada actual para obtener la predicción.

3. **Cálculo de la Pérdida:**
   - Se calcula la función de pérdida $J(\theta)$ que mide la discrepancia entre la predicción del modelo y la salida deseada.

4. **Cálculo del Gradiente:**
   - Se calcula el gradiente de la función de pérdida con respecto a los parámetros $\theta$.
   - La derivada parcial de $J(\theta)$ con respecto a cada parámetro $\theta_i$ indica cómo cambia la pérdida con un pequeño cambio en $\theta_i$.

5. **Actualización de Pesos:**
   - Se actualizan los pesos utilizando la regla de actualización del gradiente descendente:
     $\theta_i = \theta_i - \alpha \frac{\partial J(\theta)}{\partial \theta_i}$
     donde $\alpha$ es la tasa de aprendizaje, un hiperparámetro que controla el tamaño de los pasos de actualización.

6. **Iteración:**
   - Se repiten los pasos 2-5 para múltiples ejemplos de entrenamiento y durante varias épocas hasta que la función de pérdida converja a un valor mínimo o se detenga según algún criterio predefinido.

El cálculo del gradiente se realiza comúnmente mediante la retropropagación (backpropagation) en redes neuronales. La retropropagación calcula las derivadas parciales de la función de pérdida con respecto a los pesos de la red, permitiendo así la actualización de los pesos en la dirección que minimiza la pérdida. Este proceso se repite hasta que la red converge a un conjunto de pesos que produce una pérdida aceptable. Es importante ajustar la tasa de aprendizaje ($\alpha$) para garantizar un equilibrio entre la convergencia y la estabilidad del algoritmo.