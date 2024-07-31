import { Queue, Job } from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData);

    job
      .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
      .on('complete', () => console.log('Notification job completed'))
      .on('failed', (err) =>
        console.log(
          `Notification job ${job.id} failed: ${err.message || err.toString()}`
        )
      )
      .on('progress', (progress, _) =>
        console.log(`Notification job ${job.id} ${progress}% complete`)
      );

    job.save();
  }
};

export default createPushNotificationsJobs;
