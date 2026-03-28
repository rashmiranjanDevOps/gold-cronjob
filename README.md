# 🧠 DevOps Practice Notebook

## Kubernetes CronJob + Docker + AWS SNS (Deep Understanding)

---

# 🎯 Goal of This Practice

Build a system that:

* Runs automatically on schedule
* Fetches real-time gold price
* Sends notification via email

👉 This is a **real-world automation use case**

---

# 🔁 FULL FLOW 

```
Code → Docker Build → Docker Push → K8s Deploy → Run → Logs → Cleanup
```

---

# 🧩 COMPLETE ARCHITECTURE (UNDERSTAND THIS FIRST)

```
CronJob (Scheduler)
   ↓
Job (Execution request)
   ↓
Pod (Runtime unit)
   ↓
Container (Docker Image)
   ↓
Python App
   ↓
Gold API (External Service)
   ↓
AWS SNS
   ↓
Email Notification
```

---

# 📁 PROJECT STRUCTURE (WHY IMPORTANT?)

```
gold-cronjob/
├── src/app.py
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── cronjob.yaml
│   └── secret.yaml
```

👉 Why this structure?

* `src/` → separates code
* `Dockerfile` → packaging instructions
* `k8s/` → infrastructure files
* Clean structure = professional project

---

# 🟡 STEP 1: AWS SNS (NOTIFICATION SYSTEM)

## What is SNS?

👉 SNS = Pub/Sub messaging service

```
Publisher → Topic → Subscriber
```

---

## What you do:

* Create topic
* Add email subscription
* Confirm email

---

## 🧠 What happens internally?

```
Your app → sends message
SNS → receives message
SNS → delivers to email
```

---

## Why SNS?

* Decouples system
* Easy notification
* Scalable

---

# 🔐 STEP 2: IAM USER (PERMISSION SYSTEM)

## Why needed?

👉 Your container must be allowed to talk to AWS

---

## What you create:

* IAM User
* Access Key + Secret

---

## 🧠 Internal working:

```
boto3 → signs request
AWS → verifies signature
IAM → checks permission
→ allows SNS publish
```

---

# 🐳 STEP 3: DOCKER BUILD (CONTAINERIZATION)

```
docker build -t <username>/gold-cronjob:latest .
```

---

## What is Docker doing?

👉 Converts your app into a **portable package**

---

## 🧠 Internal process:

```
Dockerfile → instructions
   ↓
Base image pulled
   ↓
Dependencies installed
   ↓
Code copied
   ↓
Image created
```

---

## 🔬 Important concept: Layers

```
Each instruction = layer
```

👉 Benefits:

* Faster builds
* Caching
* Efficiency

---

# 🔐 STEP 4: DOCKER LOGIN

```
docker login
```

👉 Authenticates with Docker Hub

---

# 🚀 STEP 5: DOCKER PUSH

```
docker push <username>/gold-cronjob:latest
```

---

## 🧠 Internal process:

```
Image → split into layers
Layers → uploaded to Docker Hub
Metadata → stored
```

---

## Why push?

👉 Kubernetes cannot use local image
👉 Needs remote registry

---

# 🔐 STEP 6: KUBERNETES SECRET

```
kubectl apply -f k8s/secret.yaml
```

---

## Why secrets?

👉 Never hardcode:

* AWS keys
* API keys

---

## 🧠 Internal working:

```
Secret stored in etcd
Injected into container as ENV variables
```

---

## In Python:

```
os.getenv("API_KEY")
```

---

# ⏰ STEP 7: CRONJOB (AUTOMATION)

```
kubectl apply -f k8s/cronjob.yaml
```

---

## What is CronJob?

👉 Runs tasks on schedule (like Linux cron)

---

## Flow:

```
CronJob → Job → Pod → Container
```

---

## Schedule example:

```
*/2 * * * *
```

👉 Every 2 minutes

---

# ⚡ STEP 8: MANUAL TRIGGER (TESTING)

```
kubectl create job --from=cronjob/gold-price-cronjob test-job
```

---

## Why needed?

* No waiting for schedule
* Faster debugging

---

# 📦 STEP 9: POD CREATION (CORE)

```
kubectl get pods
```

---

## 🧠 Internal flow:

```
Scheduler → selects node
kubelet → runs pod
Container runtime → starts container
```

---

# 🌐 IMAGE PULL

```
Node → pulls image from Docker Hub
```

---

# 🚀 STEP 10: CONTAINER EXECUTION

Inside container:

```
python app.py
```

---

## 🧠 Full runtime flow:

```
App starts
   ↓
Calls API (HTTP request)
   ↓
Receives JSON
   ↓
Extracts gold price
   ↓
Sends to SNS
   ↓
Email sent
   ↓
App exits
```

---

# 📜 STEP 11: LOGS (DEBUGGING)

```
kubectl logs <pod-name>
```

---

## Why logs?

* Debug errors
* Check API response
* Verify SNS

---

# 📊 STEP 12: JOB STATUS

```
kubectl get jobs
```

---

## Status meaning:

* Running → executing
* Completed → success
* Failed → error

---

# 📩 STEP 13: EMAIL DELIVERY

```
App → SNS → Email
```

👉 Final output:

```
Gold Price Today: XXXX INR
```

---

# 🧹 STEP 14: CLEANUP

```
kubectl delete jobs --all
kubectl delete cronjob gold-price-cronjob
kubectl delete secret app-secret
```

---

## Why cleanup?

* Avoid clutter
* Save resources
* Good practice

---

# 🐳 STEP 15: DOCKER CLEANUP

```
docker rmi <username>/gold-cronjob:latest
```

---

# 🧠 FINAL UNDERSTANDING (VERY IMPORTANT)

```
CronJob triggers
   ↓
Job created
   ↓
Pod runs
   ↓
Container executes
   ↓
Python fetches data
   ↓
SNS sends message
   ↓
Email delivered
   ↓
Pod exits → Completed
```

---

# ⚠️ COMMON MISTAKES

* Missing API key
* Wrong Docker image
* Not pushing image
* Secret not applied
* Email not subscribed

---

# 🎯 PRACTICE GOAL

Repeat until you can:

* Build without notes
* Explain flow clearly
* Debug any issue

---
